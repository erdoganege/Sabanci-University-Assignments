function new_img = lab2sharpen(img, alpha, M)
% Ensuring grey scale image
[row,col,ch] = size(img);

if(ch == 3)
    img = rgb2gray(img);
end

% % Choose smoothing filter according to parameter M
k = 3;
if M == 0
    S = lab1locbox(img, k);
elseif M == 1
    S = lab2gaussfilt(img);
else
    S = lab2medfilt(img, k);
end

data = double(img);
data_S = double(S);

new_img_data = data + alpha*(data - data_S); %Apply Sharpening formula
new_img = uint8(new_img_data);

% Plots
figure();
subplot(1,2,1);
imshow(img);
title("Original Image");

subplot(1,2,2);
imshow(new_img);
if M == 0
    title({"Sharpened Image with Box Filter"; "Alpha: " + alpha + " Window Size: " + k+'x'+k});
elseif M == 1
    title({"Sharpened Image with Gaussian Filter"; "Alpha: " + alpha});
else
    title({"Sharpened Image with Median Filter"; "Alpha: " + alpha + " Window Size: " + k+'x'+k});
end
    
    