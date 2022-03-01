% Load the files given in SUcourse as Seq variable
load("traffic.mat");
load("cars1.mat");
load("cars2.mat");
load("rubic.mat");
load("sphere.mat");
load("taxi.mat");

Seq = cars2;
[row,col,num]=size(Seq);
% Define k and Threshold
% k = 10;
% k = 20;
k = 30;
% Threshold = 1000;
Threshold = 100000;
% Threshold = 500000;
for j=2:1:num
ImPrev = Seq(:,:,j-1);
ImCurr = Seq(:,:,j);
lab7OF(ImPrev,ImCurr,k,Threshold);
pause(0.1);
end


