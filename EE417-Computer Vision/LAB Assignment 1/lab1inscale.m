function new_img = lab1inscale(img)

[row,col,ch] = size(img);
Card = row*col;

if(ch == 3)
    img = rgb2gray(img);
end

data = double(img);
Gmax = 255;

a = -min(data(:));
b = Gmax / (max(data(:)) + a);

new_img_data = b * (data + a);

new_img = uint8(new_img_data);

figure();
subplot(2,2,1);
imshow(img);
title("Original Image")

subplot(2,2,3);
imhist(img);
title("Histogram of the Original Image Umin = " + min(data(:)) + " Umax = " + max(data(:)))

subplot(2,2,2);
imshow(new_img);
title("Linearly Scaled Image")

subplot(2,2,4);
imhist(new_img);
title("Histogram of the Linearly Scaled Image Umin = "  + min(new_img_data(:)) + " Umax = " + max(new_img_data(:)))

end