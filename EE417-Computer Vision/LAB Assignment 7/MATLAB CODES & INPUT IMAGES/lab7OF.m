function lab7OF(ImPrev,ImCurr,k,Threshold)
% Smooth the input images using a Box filter
box_filter = [1,1,1;1,1,1;1,1,1];
ImPrev = conv2(ImPrev, box_filter, 'same');
ImCurr = conv2(ImCurr, box_filter, 'same');

% % Smooth the input image using a Gaussian Filter 3x3
% ImPrev = imgaussfilt(double(ImPrev), [3, 3]);
% ImCurr = imgaussfilt(double(ImCurr), [3, 3]);

% % Smooth the input image using a Gaussian Filter 9x9
% ImPrev = imgaussfilt(double(ImPrev), [9, 9]);
% ImCurr = imgaussfilt(double(ImCurr), [9, 9]);

% Calculate spatial gradients (Ix, Iy) using Prewitt filter
x_filter = [-1,0,1; -1,0,1; -1,0,1];
y_filter = [-1,-1,-1; 0,0,0; 1,1,1];
Ix = conv2(ImCurr, x_filter, 'same');
Iy = conv2(ImCurr, y_filter, 'same');
% Calculate temporal (It) gradient
It = ImPrev - ImCurr;

[ydim,xdim] = size(ImCurr);
Vx = zeros(ydim,xdim);
Vy = zeros(ydim,xdim);
G = zeros(2,2);
b = zeros(2,1);
cx=k+1;
for x=k+1:k:xdim-k-1
cy=k+1;
for y=k+1:k:ydim-k-1
    my_window_x = Ix((y-k):(y+k), (x-k):(x+k));
    my_window_y = Iy((y-k):(y+k), (x-k):(x+k));
    my_window_t = It((y-k):(y+k), (x-k):(x+k));
    G(1,1) = sum(sum(my_window_x.*my_window_x));
    G(1,2) = sum(sum(my_window_x.*my_window_y));
    G(2,1) = G(1,2);
    G(2,2) = sum(sum(my_window_y.*my_window_y));
    b(1,1) = sum(sum(my_window_x.*my_window_t));
    b(2,1) = sum(sum(my_window_y.*my_window_t));
% Calculate the elements of G and b
if (min(eig(G)) < Threshold)
Vx(cy,cx)=0;
Vy(cy,cx)=0;
else
% Calculate u
u = (inv(G)*b)*-1;
Vx(cy,cx)=u(1);
Vy(cy,cx)=u(2);
end
cy=cy+k;
end
cx=cx+k;
end
cla reset;
imagesc(ImPrev); hold on;
[xramp,yramp] = meshgrid(1:1:xdim,1:1:ydim);
quiver(xramp,yramp,Vx,Vy,10,"r");
colormap gray;
end