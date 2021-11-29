function new_img = lab2sigma(img, var, k)
% Ensuring grey scale image
[row,col,ch] = size(img);

if(ch == 3)
    img = rgb2gray(img);
end

data = double(img);

new_img_data = zeros(row, col);

% % Double for loop for sliding window
window_size = k;
for i = window_size+1:row-window_size
    for j = window_size+1:col-window_size
        my_window = data((i-window_size):(i+window_size), (j-window_size):(j+window_size)); %Taking window
        [H, bin] = imhist(uint8(my_window)); %Histogram of the taken window
        upper_bound = data(i, j) + var; %Defining interval's upper bound
        lower_bound = data(i, j) - var; %Defining interval's lower bound
        if lower_bound < 0  %Lower bound cannot be lower than zero
            lower_bound = 0;
        end
        if upper_bound > 255 %Upper bound cannot be larger than 255
            upper_bound = 255;
        end
        S = 0;
        summation = 0;
        for u = lower_bound:upper_bound   %Calculating mean of the pixels that are in the interval
            summation = summation + (u * H(u+1)); %Summation part of the formula
            S = S + H(u+1);  %Number of elements that are in the interval
        end
        my_mean = summation / S; % Mean of the interval
        new_img_data(i, j) = my_mean;        
    end
end
new_img = uint8(new_img_data);
% Plots
figure();
subplot(2,1,1);
imshow(img);
title("Original Image");

subplot(2,1,2);
imshow(new_img);
title({"Sigma Filtered Image with window " + k+' x '+k; "Deviation (sigma) = " + var});


