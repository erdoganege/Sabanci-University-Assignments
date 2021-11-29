checker = imread("checker.jpg");
circles = imread('circlesBrightDark.png');
wrench = imread("wrench.jpg");
balls = imread("balls.jpg");

% % Line Detection
lab5houghlines(checker);
% lab5houghlines(wrench);


% % Circile Detection
lab5houghcircles(circles, 0.9);
% lab5houghcircles(circles, 0.2);
% lab5houghcircles(circles, 1);
% lab5houghcircles(balls, 0.9);

% figHandles = findall(0,'Type','figure');
% temp = size(figHandles);
% for i = temp(1):-1:1
% path = "C:\Users\user\Desktop\erdoganege_EE417_POSTLAB5\figure" +i;
% saveas(figHandles(i),path);
% end
