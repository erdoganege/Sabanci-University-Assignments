function [new_img, new_img2] = lab2sobelfilt(img)

% Ensuring grey scale image
[row,col,ch] = size(img);

if(ch == 3)
    img = rgb2gray(img);
end

%Define both filters
xfilter = [[-1, 0, 1]; 
           [-2, 0, 2];
           [-1, 0, 1]];
       
yfilter = [[1, 2, 1]; 
           [0, 0, 0];
           [-1, -2, -1]];
       
data = double(img);

new_img_data = zeros(row, col);
new_img_data2 = zeros(row, col);

% % Double for loop for sliding window
window_size = 1;
for i = window_size+1:row-window_size
    for j = window_size+1:col-window_size
        my_window = data((i-window_size):(i+window_size), (j-window_size):(j+window_size));%take the window
        x_value = sum(sum(my_window .* xfilter)); %Convolution operation
        y_value = sum(sum(my_window .* yfilter)); %Convolution operation
        new_img_data(i, j) = x_value;
        new_img_data2(i, j) = y_value;
    end
end
new_img = uint8(new_img_data);
new_img2 = uint8(new_img_data2);

% Plots
figure();
subplot(2,2,[1,2]);
imshow(img);
title("Original Image");

subplot(2,2,3);
imshow(new_img);
title("Sobel Vertical Filtered Image");

subplot(2,2,4);
imshow(new_img2);
title("Sobel Horizontal Filtered Image");
