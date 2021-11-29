function lab5houghcircles(img, sensitivity)
% Ensuring grey scale image
new_img = img;
[row,col,ch] = size(img);
if(ch == 3)
    img = rgb2gray(img);
end
Rmin = 20;
Rmax = 60;
[centers, radii, metric] = imfindcircles(img,[Rmin, Rmax]);
figure()
subplot(1,3,1)
imshow(img)
viscircles(centers, radii, 'Color','b');
title("Detected Circles using Hough Transform "+Rmin + " <= Radius <= " + Rmax)
subplot(1,3,2)
imshow(img)
[centers, radii, metric] = imfindcircles(img,[Rmin, Rmax], "Sensitivity", sensitivity);
viscircles(centers, radii, 'Color','r');
title("Detected Circles using Hough Transform "+Rmin + " <= Radius <= " + Rmax + " & Sensitivity = "+ sensitivity)
subplot(1,3,3)
imshow(img)
[centers, radii, metric] = imfindcircles(img,[Rmin, Rmax], "Sensitivity", sensitivity);
viscircles(centers, radii, 'Color','b');
[centers, radii, metric] = imfindcircles(img,[Rmin, Rmax], "Sensitivity", sensitivity, "ObjectPolarity", "Dark");
viscircles(centers, radii, 'Color','r',  "LineStyle", "--");
title("Detected Bright and Dark Circles "+Rmin + " <= Radius <= " + Rmax + " & Sensitivity = "+ sensitivity)