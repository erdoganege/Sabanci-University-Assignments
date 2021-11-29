function lab5houghlines(img)
% Ensuring grey scale image
new_img = img;
[row,col,ch] = size(img);
if(ch == 3)
    img = rgb2gray(img);
end

BW = edge(img,'canny');
[H,T,R] = hough(BW,'RhoResolution',0.5,'Theta',-90:0.5:89);

figure()
subplot(2,2,1);
imshow(new_img);
title('Original Image');

subplot(2,2,2);
imshow(BW);
title('Edges');

subplot(2,2,[3,4]);
imshow(imadjust(rescale(H)),'XData',T,'YData',R,...
      'InitialMagnification','fit');
title('Hough Transform');
xlabel('\theta'), ylabel('\rho');
axis on, axis normal, hold on;

peaks = 20;
P  = houghpeaks(H,peaks);
figure()
imshow(H, [] ,'XData',T,'YData',R,...
      'InitialMagnification','fit');
xlabel('\theta'), ylabel('\rho');
axis on, axis normal, hold on;
plot(T(P(:,2)),R(P(:,1)),'s','color','white');
title(peaks + " Peaks Hough Transform with Default (0.5) of maximum Hough points Threshold")
% Find lines and plot them
fillgap = 10;
minlength = 40;
lines = houghlines(BW,T,R,P,'FillGap',fillgap,'MinLength',minlength);
figure() 
imshow(img); 
hold on
max_len = 0;
min_len = 9999999;
for k = 1:length(lines)
 xy = [lines(k).point1; lines(k).point2];
 plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');
 % plot beginnings and ends of lines
 plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','green');
 plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');
 % determine the endpoints of the longest and shortest line segment 
 len = norm(lines(k).point1 - lines(k).point2);
 if ( len > max_len)
   max_len = len;
   xy_long = xy;
 end
 if (len < min_len)
    min_len = len;
    xymin_long = xy;
 end
end

% highlight the longest line segment
plot(xy_long(:,1),xy_long(:,2),'LineWidth',2,'Color','cyan');

% highlight the shortest line segment
plot(xymin_long(:,1),xymin_long(:,2),'LineWidth',2,'Color','red');
title({"Found Longest and Shortest Lines, FillGap "+ fillgap + ", MinLength "+minlength; "Length of Maximum Line: "+max_len + " Length of Minimum Line: " + min_len});




