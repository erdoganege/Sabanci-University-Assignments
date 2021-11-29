function new_img = lab1locbox(img, window_size)

[row,col,ch] = size(img);

if(ch == 3)
    img = rgb2gray(img);
end

data = double(img);
new_img_data = data;

for i = window_size+1:row-window_size
    for j = window_size+1:col-window_size
        my_window = data((i-window_size):(i+window_size), (j-window_size):(j+window_size));
        
        mean_my_window = mean(my_window(:));
        new_img_data(i, j) = mean_my_window;
    end
end
new_img = uint8(new_img_data);

figure();
subplot(2,1,1);
imshow(img);
title("Original Image");

subplot(2,1,2);
imshow(new_img);
title("Box Filtered Image, k = " + window_size);

