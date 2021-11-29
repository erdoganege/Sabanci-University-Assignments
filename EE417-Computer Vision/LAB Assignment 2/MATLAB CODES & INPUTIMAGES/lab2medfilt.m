function new_img = lab2medfilt(img, k)

% Ensuring grey scale image
[row,col,ch] = size(img);

if(ch == 3)
    img = rgb2gray(img);
end

% % Gaussian Smoothed image
gaussian_img = lab2gaussfilt(img);

data = double(img);
new_img_data = zeros(row, col);

% % Double for loop for sliding window
window_size = k;
for i = window_size+1:row-window_size
    for j = window_size+1:col-window_size
        my_window = data((i-window_size):(i+window_size), (j-window_size):(j+window_size));
        median_value = myMedian(my_window); %Finding median of the window
        new_img_data(i, j) = median_value;
    end
end
new_img = uint8(new_img_data);
% Plots
figure();
subplot(1,3,1);
imshow(img);
title("Original Image");

subplot(1,3,2);
imshow(gaussian_img);
title("Gaussian Filtered Image");

subplot(1,3,3);
imshow(new_img);
title({"Median Filtered Image"; "k ="+ k});