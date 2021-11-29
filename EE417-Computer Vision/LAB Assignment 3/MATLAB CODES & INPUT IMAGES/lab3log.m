function new_img = lab3log(img, Threshold, Threshold2)

% Ensuring grey scale image
[row,col,ch] = size(img);
if(ch == 3)
    img = rgb2gray(img);
end

gauss_filt = lab2gaussfilt(img);

kernel = [0,1,0; 1,-4,1; 0,1,0];

data = double(gauss_filt);
% data = double(img);
% % Double for loop for sliding window
window_size = 1;
new_img_data = zeros(row, col);
for i = window_size+1:row-window_size %Edges are zero
    for j = window_size+1:col-window_size
        my_window = data((i-window_size):(i+window_size), (j-window_size):(j+window_size)); %take the window
        value = sum(sum(my_window .* kernel)); %Convolution operation
        new_img_data(i, j) = value;
    end
end
new_img = uint8(new_img_data);

segment = new_img_data(150, 30:60); 
% Our borders in the image have not affected from Gaussian. To fix it.
new_img_data(:, 1:3) = 0;
new_img_data(1:3 ,:) = 0;
new_img_data(end-2:end, :) = 0;
new_img_data(:, end-2:end) = 0;
[row2, col2, ch2] = size(new_img_data);
new_img_data_Edges = zeros(row2,col2); 
for i = 2:row-1 
    for j = 2:col-1
        center = new_img_data(i, j);
        left = new_img_data(i, j-1);
        right = new_img_data(i, j+1);
        upper = new_img_data(i-1, j);
        down = new_img_data(i+1, j);
        upper_left = new_img_data(i-1, j-1);
        upper_right = new_img_data(i-1, j+1);
        down_left = new_img_data(i+1, j-1);
        down_right = new_img_data(i+1, j+1);
        
        if (center > Threshold2)
%       Case 1 left/right zero crossing
        if (left*right < 0) %Sign Change
            if (abs(left - right) > Threshold)
                new_img_data_Edges(i, j) = 255;
            end   
 %      Case 2 up/down zero crossing
        elseif (upper*down < 0) %Sign Change
            if (abs(upper - down) > Threshold)
                new_img_data_Edges(i, j) = 255;
            end
  %     Case 3 Diaganols
        elseif (upper_left*down_right < 0) %Sign Change
            if (abs(upper_left - down_right) > Threshold)
                new_img_data_Edges(i, j) = 255;
            end       
        elseif (upper_right*down_left < 0) %Sign Change
            if (abs(upper_right - down_left) > Threshold)
                new_img_data_Edges(i, j) = 255;
            end
        elseif (center*upper_left < 0) %Sign Change
            if (abs(center - upper_left) > Threshold)
                new_img_data_Edges(i, j) = 255;
            end
        elseif (center*upper_right < 0) %Sign Change
            if (abs(center - upper_right) > Threshold)
                new_img_data_Edges(i, j) = 255;
            end
        end 
        end
    end
end

new_img_Edges = uint8(new_img_data_Edges);



% % Plots
% figure();
% subplot(2,2,1);
% imshow(img);
% title("Original Image");
% 
% subplot(2,2,2);
% imshow(new_img);
% title("LOG Filtered Image");
% 
% subplot(2,2, 4);
% imshow(new_img_Edges);
% title("LOG Edges Image");
% 
% subplot(2,2,3);
% plot(30:60, segment);
% title("Gradient Profile");
% xlabel("Pixel Location");
% ylabel("Gradient Magnitude");

figure();
subplot(1,2,1);
imshow(img);
title("Original Image");

subplot(1,2, 2);
imshow(new_img_Edges);
title({"LOG Edges Image"; "Threshold for pixel = "+ Threshold2; "Threshold for magnitude = "+ Threshold});


