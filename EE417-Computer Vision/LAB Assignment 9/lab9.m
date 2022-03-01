clear all; close all; clc;
%% Definitions
%rng(1);
L = 300;
I1 = zeros(L,L);

f=L;
u0 = L/2;
v0 = L/2;

K = [f 0 u0;    
    0 f v0;
    0 0 1];

DEG_TO_RAD = pi/180;

%% World Coordinates
% we need to select 8 points since min 8 points is needed to estimate the
% essential matrix E
P_W=[
%     0	2	0	1;
%     0	1	0	1;
%     0	0	0	1;
    0	2	-1	1;
    0	1	-1	1;
%     0	0	-1	1;
    0	2	-2	1;
    0	1	-2	1;
%     0	0	-2	1;
%     1	0	0	1;
%     2	0	0	1;
    1	0	-1	1;
    2	0	-1	1;
    1	0	-2	1;
    2	0	-2	1;
%     1	1	0	1;
%     2	1	0	1;
%     1	2	0	1;
%     2	2	0	1
    ];

P_W = P_W';
NPTS = size(P_W,2); %Number of points

%% Visualization
figure;
subplot(1,3,1)
wally = meshgrid(0:0.1:3); 
wallz = meshgrid(-3:0.1:0); 
wallx = 0*ones(size(wallz,1));
surf(wallx, wally, wallz','FaceColor',(1/255)*[97 178 205],'EdgeColor','none') 
hold on
wallx = meshgrid(0:0.1:3); 
wallz = meshgrid(-3:0.1:0); 
wally = 0*ones(size(wallz,1)); 
surf(wallx, wally, wallz','FaceColor',(1/255)*[77 137 157],'EdgeColor','none') 
wallx = meshgrid(0:0.1:3); 
wally = meshgrid(0:0.1:3); 
wallz = zeros(size(wally,1)); % Generate z data
surf(wallx, wally', wallz,'FaceColor',(1/255)*[45 162 200],'EdgeColor','none') 
plot3(P_W(1,:),P_W(2,:),P_W(3,:),'b.','MarkerSize',36);
axis equal;
grid on
axis vis3d;
axis([-3 3 -3 3 -3 3])
grid on
xlabel('x')
ylabel('y')
zlabel('z')

%% Camera Transformation for View 1
ax = 120 * DEG_TO_RAD;
ay = 0 *DEG_TO_RAD;
az = 60 * DEG_TO_RAD;

Rx = [1 0 0;
      0 cos(ax) -sin(ax);
      0 sin(ax) cos(ax)];
Ry = [cos(ay)  0  sin(ay);
           0   1     0;
      -sin(ay) 0  cos(ay)];
Rz = [cos(az) -sin(az) 0;
      sin(az) cos(az)  0;
      0          0     1];
  
Rc1 = Rx*Ry*Rz;
Tc1 = [0;0;5];
M = [Rc1 Tc1];

p1 = K*(M * P_W);
noise1 = 4*rand(3,NPTS)-2;
noise1(3,:)=1;
p1 = p1 + noise1;

u1(1,:) = p1(1,:) ./ p1(3,:);
u1(2,:) = p1(2,:) ./ p1(3,:);
u1(3,:) = p1(3,:) ./ p1(3,:);

for i=1:length(u1)
    x = round(u1(1,i)); y=round(u1(2,i));
    I1(y-2:y+2, x-2:x+2) = 255;
end

subplot(1,3,2), imshow(I1, []), title('View 1', 'FontSize',20);

%% Camera Transformation for View 2
ax = 0 * DEG_TO_RAD;
ay = -25 *DEG_TO_RAD;
az = 0 * DEG_TO_RAD;

Rx = [1 0 0;
      0 cos(ax) -sin(ax);
      0 sin(ax) cos(ax)];
Ry = [cos(ay)  0  sin(ay);
           0   1     0;
      -sin(ay) 0  cos(ay)];
Rz = [cos(az) -sin(az) 0;
      sin(az) cos(az)  0;
      0          0     1];

Rc2c1 = Rx*Ry*Rz;
TrueR = Rc2c1;
Tc2c1 = [3;0;1];
TrueT = Tc2c1;
Hc1 = [Rc1 Tc1; 0 0 0 1];
Hc2c1 = [Rc2c1 Tc2c1; 0 0 0 1];
Hc2 = Hc2c1*Hc1;

Rc2 = Hc2(1:3,1:3);
Tc2 = Hc2(1:3,4);

M = [Rc2 Tc2];

I2 = zeros(L,L);
p2 = K*(M*P_W);

noise2 = 4*rand(3,NPTS)-2;
noise2(3,:)=1;
p2 = p2 + noise2;

u2(1,:) = p2(1,:) ./ p2(3,:);
u2(2,:) = p2(2,:) ./ p2(3,:);
u2(3,:) = p2(3,:) ./ p2(3,:);

for i=1:length(u2)
    x = round(u2(1,i)); y=round(u2(2,i));
    I2(y-2:y+2, x-2:x+2) = 255;
end

subplot(1,3,3), imshow(I2, []), title('View 2', 'FontSize',20);

t = Tc2c1;
T_skew = [0 -t(3) t(2); t(3) 0 -t(1); -t(2) t(1) 0];
Etrue = T_skew*Rc2c1;

%% Displaying the information
disp('u1: Pixel coordinates in view 1')
u1info = ['Size of u1 is ' num2str(size(u1,1)) 'x' num2str(size(u1,2))];
disp(u1info)
disp('u2: Pixel coordinates in view 2')
u2info = ['Size of u2 is ' num2str(size(u2,1)) 'x' num2str(size(u2,2))];
disp(u2info)
disp('-------------')
%% Lab#8 Assignment starts here.
%% Transform pixel coordinates and construct X matrix using Equations 1 and 2
K_inv = inv(K);
u1_new = K_inv * u1;
u2_new = K_inv * u2;

% Picking 8 poins

for i = 1:8
    a(i,:) = [u1_new(1,i)*u2_new(1,i), u1_new(1,i)*u2_new(2,i), u1_new(1,i)*u2_new(3,i), u1_new(2,i)*u2_new(1,i), u1_new(2,i)*u2_new(2,i), u1_new(2,i)*u2_new(3,i), u1_new(3,i)*u2_new(1,i), u1_new(3,i)*u2_new(2,i), u1_new(3,i)*u2_new(3,i)];
end

X = [];
for i = 1:8
    X = [X; a(i,:)];
end

% % Picking all poins

% for i = 1:19
%     a(i,:) = [u1_new(1,i)*u2_new(1,i), u1_new(1,i)*u2_new(2,i), u1_new(1,i)*u2_new(3,i), u1_new(2,i)*u2_new(1,i), u1_new(2,i)*u2_new(2,i), u1_new(2,i)*u2_new(3,i), u1_new(3,i)*u2_new(1,i), u1_new(3,i)*u2_new(2,i), u1_new(3,i)*u2_new(3,i)];
% end
% 
% X = [];
% for i = 1:19
%     X = [X; a(i,:)];
% end

%% Estimate E, cure it and check for Essential Matrix Characterization 
[U, S, V] = svd(X'*X);
E = V(:, 9);
E_new = [E(1), E(4), E(7);
        E(2), E(5), E(8);
        E(3), E(6), E(9)];
[U2, S2, V2] = svd(E_new);
S2(1,1) = 1;
S2(2,2) = 1;
S2(3,3) = 0;

E_est = U2*S2*V2';

disp("Determinant of U:");
det(U2)
disp("Determinant of V:");
det(V2)
%% Find epipoles and epipolar lines
epipol1 = null(E_est);
epipol2 = null(E_est');

line1 = E_est' * u2_new(:,1);
line2 = E_est * u1_new(:,1);

%% Verify epipoles and epipolar lines
ver1 = line1'*epipol1;
ver2 = line2'*epipol2;
disp("First Verification:")
disp(ver1)
disp("Second Verification:")
disp(ver2)

%% Recover the rotation and the translation
Rz = [0, -1, 0;
      1, 0, 0;
      0, 0, 1];

T1_ = U2*Rz*S2*U2';
R1 = U2*Rz'*V2';

Rz2 = [0,1,0;
       -1, 0,0;
       0,0,1];
T2_ = U2*Rz2*S2*U2';
R2 = U2*Rz2'*V2';

T1 = [T1_(3,2); T1_(1,3); T1_(2,1)];
T2 = [T2_(3,2); T2_(1,3); T2_(2,1)];


%% Compare your results with ground truth
disp('True E =')
disp(Etrue)
disp('Estimated E = ')
disp(E_est)
disp('-------------')
disp('-------------')

% R should be exactly similar, but one of them only since the other means
% the case when the camera is behind the view
disp('True R =')
disp(TrueR)
disp('Estimated R1 & R2 :')
disp('R1_est = ')
disp(R1)
disp('-------------')
disp('R2_est = ')
disp(R2)
disp('-------------')
disp('-------------')

% T should be scaled version of True T, since we cannot find a unique T and
% it is always up to scale
disp('True T =')
disp(TrueT)
disp('Estimated T1 & T2 :')
disp('T1_est = ')
disp(T1)
disp('-------------')
disp('T2_est = ')
disp(T2)
disp('-------------')