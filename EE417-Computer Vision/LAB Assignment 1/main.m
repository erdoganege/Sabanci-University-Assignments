% % Histogram Equalization Part
city = imread("city.png");

eq_city = histeq(city);

figure();
subplot(2,2,1);
imshow(city);
title("Original Image")

subplot(2,2,3);
imhist(city);
title("Histogram of Original Image")

subplot(2,2,2);
imshow(eq_city);
title("Equalized Image")

subplot(2,2,4);
imhist(eq_city);
title("Histogram of Equalized Image")

% % Linearly Scaling Part

linearly_scaled = lab1inscale(city);

% % Condional Scaling Part

board = imread("board.jpg");
cond_scaled = lab1condscale(city, board);

% % Local Mean Filter 
jump = imread("jump.png");
window_size = 5;
loc_boxed = lab1locbox(jump, window_size);

% % Local MaxMin Filter 
currentImage = imread("currentImage.png");
window_size = 3;
[min_boxed, max_boxed] = lab1locmaxmin(currentImage, window_size);



