function new_img = lab2gaussfilt(img)

% Ensuring grey scale image
[row,col,ch] = size(img);
if(ch == 3)
    img = rgb2gray(img);
end

% Define Kernel
kernel = [ [1,4,7,4,1];
           [4, 16, 26, 16, 4];
           [7, 26, 41, 26, 7];
           [4, 16, 26, 16, 4];
           [1,4,7,4,1]];   
kernel = kernel / 273;
       
window_size = 2;

data = double(img);
% % Double for loop for sliding window
new_img_data = zeros(row, col);
for i = window_size+1:row-window_size %Edges are zero
    for j = window_size+1:col-window_size
        my_window = data((i-window_size):(i+window_size), (j-window_size):(j+window_size)); %take the window
        smoothed_value = sum(sum(my_window .* kernel)); %Convolution operation
%         temp = my_window .* kernel;
%         smoothed_value = sum(temp(:));
        new_img_data(i, j) = smoothed_value;
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
title("Gaussian Filtered Image");
