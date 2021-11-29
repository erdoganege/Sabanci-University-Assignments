peppers = imread("peppers.png");
contour = imread("Object_contours.jpg");
blocks = imread("blocks.png");

% % Prewitt Part
new_img = lab3prewitt(peppers, 100);
% new_img = lab3prewitt(peppers, 20);
% new_img = lab3prewitt(blocks, 100);
% new_img = lab3prewitt(blocks, 20);


% %  Sobel Part
new_img = lab3sobel(peppers, 100);
% new_img = lab3sobel(peppers, 20);
% new_img = lab3sobel(blocks, 100);
% new_img = lab3sobel(blocks, 20);


% % Comparison Prewitt and Sobel
new_img = lab3prewitt(peppers, 10);
% new_img = lab3sobel(peppers, 10);


% % Laplacian Part

new_img = lab3log(contour,10, 3);
% new_img = lab3log(contour,20, 3);
% new_img = lab3log(contour,30, 3);
% 
% new_img = lab3log(contour,10, 5);
% new_img = lab3log(contour,20, 5);
% new_img = lab3log(contour,30, 5);
% 
% new_img = lab3log(peppers,2, 3);
% new_img = lab3log(peppers,10, 3);
% new_img = lab3log(peppers,20, 3);
% 
% new_img = lab3log(peppers,2, 5);
% new_img = lab3log(peppers,10, 5);
% new_img = lab3log(peppers,20, 5);

% figHandles = findall(0,'Type','figure'); 
% for i = 22:-1:1
% path = "C:\Users\user\Desktop\erdoganege_EE417_POSTLAB3\figure" +i;
% saveas(figHandles(i),path);
% end