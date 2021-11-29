function [new_img, new_img2] = lab1locmaxmin(img, window_size)

[row,col,ch] = size(img);

if(ch == 3)
    img = rgb2gray(img);
end

data = double(img);
new_img_data = data;
new_img_data2 = data;

for i = window_size+1:row-window_size
    for j = window_size+1:col-window_size
        my_window = data((i-window_size):(i+window_size), (j-window_size):(j+window_size));
        
        max_my_window = max(my_window(:));
        min_my_window = min(my_window(:));
        
        new_img_data(i, j) = max_my_window;
        new_img_data2(i, j) = min_my_window;
    end
end
new_img = uint8(new_img_data);
new_img2 = uint8(new_img_data2);

figure();
subplot(1,3,1);
imshow(img);
title("Original Image");

subplot(1,3,2);
imshow(new_img);
title("Local Max Filtered Image, k = " + window_size);

subplot(1,3,3);
imshow(new_img2);
title("Local Min Filtered Image, k = " + window_size);