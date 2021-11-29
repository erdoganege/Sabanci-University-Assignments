object = imread("mychecker.png");
% Ensuring grey scale image
[row,col,ch] = size(object);
if(ch == 3)
    img = rgb2gray(object);
end
img = imgaussfilt(img);
BW = edge(img,'canny');
[H,T,R] = hough(BW,'Theta',-90:0.5:89);

peaks = 20;
P  = houghpeaks(H,peaks);

% Find lines and plot them
fillgap = 20;
minlength = 20;
lines = houghlines(BW,T,R,P,'FillGap',fillgap,'MinLength',minlength);
figure() 
subplot(1,2,1)
imshow(img); 
title("Calibration Object")
subplot(1,2,2)
imshow(img);
hold on
for k = 1:length(lines)
 xy = [lines(k).point1; lines(k).point2];
 plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');   
 % plot beginnings and ends of lines
 plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
 plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');
end
title("Result of Hough line Detection")

thetas = [-81, -77.5, -85, 0.5, -0.5, 1]; %first 3 horizontal, next 3 vertical
rhos = [-287, -309, -266, 271, 231, 314];

figure()
imshow(img)
hold on
x = -500:500;
for i = 1:6
    y = (rhos(1, i) - x*cosd(thetas(1, i))) / sind(thetas(1,i));
    plot(x, y,'LineWidth',2,'Color', 'magenta')
end
C = corner(img);
plot(C(:,1),C(:,2),'bo');
intersection_list = [];
for i = 1:3
    for k = 4:6
    B = [rhos(1,i); rhos(1,k)];
    A = [cosd(thetas(1,i)), sind(thetas(1,i)); cosd(thetas(1,k)), sind(thetas(1,k))];
    inv_a = inv(A);
    intersection = inv_a* B;
    intersection_list = [intersection_list; [intersection(1,1), intersection(2,1)]];
    plot(intersection(1,1), intersection(2,1), 'r.', 'Color', 'magenta', 'MarkerSize', 25);
    end
end
title("Corners extracted by the intersection pointS of six lines and Harris corner detection algorithm")
harris_corners = [64, 62, 63, 49, 65, 46, 70, 74, 55];
actual_point_x = [269.5, 234, 308.5, 268.5, 235, 307.5, 269.5, 234.5, 309.5];
actual_point_y = [334.5, 328, 340.5, 376.5, 369, 385.5, 291.5, 288.5, 294.5];
for i = 1:9
    disp("Corner Point: "+i)
    x1 = intersection_list(i,1);
    y1 = intersection_list(i,2);
    x2 = C(harris_corners(1,i),1);
    y2 = C(harris_corners(1,i),2);
    actual_x = actual_point_x(1,i);
    actual_y = actual_point_y(1,i);
    my_distance = sqrt((x1-x2)^2 + (y1-y2)^2);
    my_distance2 = sqrt((x1-actual_x)^2 + (y1-actual_y)^2);
    my_distance3 = sqrt((x2-actual_x)^2 + (y2-actual_y)^2);
    disp("Distance between Harris Corner (blue circle) and intersection point (magenta circle): "+my_distance)
    disp("Distance between Actual Corner Point and intersection point (magenta circle): "+my_distance2)
    disp("Distance between Actual Corner Point and Harris Corner (blue circle): "+my_distance3)
end


% % For INLAB RESULTS just uncomment below part
% object = imread("calibrationObject.png");
% % Ensuring grey scale image
% [row,col,ch] = size(object);
% if(ch == 3)
%     img = rgb2gray(object);
% end
% BW = edge(img,'canny');
% [H,T,R] = hough(BW,'Theta',-90:0.5:89);
% peaks = 30;
% P  = houghpeaks(H,peaks);
% % Find lines and plot them
% fillgap = 20;
% minlength = 40;
% lines = houghlines(BW,T,R,P,'FillGap',fillgap,'MinLength',minlength);
% figure() 
% subplot(1,2,1)
% imshow(img); 
% title("Calibration Object")
% subplot(1,2,2)
% imshow(img);
% hold on
% for k = 1:length(lines)
%  xy = [lines(k).point1; lines(k).point2];
%  plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');   
%  % plot beginnings and ends of lines
%  plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
%  plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');
% end
% title("Result of Hough line Detection")
% first_beginning = [141, 132];
% first_ending = [171, 350];
% first_theta = -8;
% first_rho = 120;
% second_beginning = [39, 130];
% second_ending = [187, 186];
% second_theta = -69.5;
% second_rho = -108;
% figure()
% imshow(img)
% hold on
% x = -500:500;
% y1 = (first_rho - x*cosd(first_theta)) / sind(first_theta);
% y2 = (second_rho - x*cosd(second_theta)) / sind(second_theta);
% plot(x, y1 ,'LineWidth',2,'Color', 'magenta')
% plot(x,y2 ,'LineWidth',2,'Color', 'magenta') 
% C = corner(img);
% plot(C(:,1),C(:,2),'bo');
% 
% B = [first_rho; second_rho];
% A = [cosd(first_theta), sind(first_theta); cosd(second_theta), sind(second_theta)];
% inv_a = inv(A);
% intersection = inv_a* B;
% plot(intersection(1,1), intersection(2,1), 'r.', 'Color', 'magenta', 'MarkerSize', 25);
% x1 = intersection(1,1);
% y1 = intersection(2,1);
% x2 = C(44,1);
% y2 = C(44,2);
% actual_point_x = 146;
% actual_point_y = 171;
% my_distance = sqrt((x1-x2)^2 + (y1-y2)^2);
% my_distance2 = sqrt((x1-actual_point_x)^2 + (y1-actual_point_y)^2);
% my_distance3 = sqrt((x2-actual_point_x)^2 + (y2-actual_point_y)^2);
% disp("Distance between Harris Corner (blue circle) and intersection point (magenta circle): "+my_distance)
% disp("Distance between Actual Corner Point and intersection point (magenta circle): "+my_distance2)
% disp("Distance between Actual Corner Point and Harris Corner (blue circle): "+my_distance3)
% title("Corners extracted by the intersection point of two lines and Harris corner detection algorithm")





