% % If you want to see all output images that are in the report UNCOMMENT
% % all commented lines
jump = imread("jump.png");
tiger = imread("Tiger.png");
mother = imread("mother.png");
house = imread("house.png");
blocks = imread("blocks.png");
lizard = imread("noisylizard.jpg");
bridge = imread("TowerBridge.bmp");

% % Linear Filtering
new_img = lab2gaussfilt(jump);
% new_img = lab2gaussfilt(lizard);

% % Non Linear Filtering
new_img = lab2medfilt(tiger, 5);
% new_img = lab2medfilt(tiger, 10);
% new_img = lab2medfilt(lizard, 1);
% new_img = lab2medfilt(lizard, 10);
% new_img = lab2medfilt(blocks, 5);

% % Sharpening Part
% new_img = lab2sharpen(mother, 50, 0); 
new_img = lab2sharpen(mother, 5, 0); 
% new_img = lab2sharpen(mother, 10, 0);
% 
% new_img = lab2sharpen(mother, 5, 1); 
% new_img = lab2sharpen(mother, 10, 1); 
% 
% new_img = lab2sharpen(mother, 5, 2); 
% new_img = lab2sharpen(mother, 10, 2); 

% new_img = lab2sharpen(house, 0, 0);  
% new_img = lab2sharpen(house, 10, 0);
% 
% new_img = lab2sharpen(house, 5, 1); 
% new_img = lab2sharpen(house, 10, 1); 
% 
% new_img = lab2sharpen(house, 5, 2); 
% new_img = lab2sharpen(house, 10, 2); 



% % Sobel Filtering
[new_img, new_img2] = lab2sobelfilt(house);
% [new_img, new_img2] = lab2sobelfilt(blocks);
% 
% smoothed_house = lab2gaussfilt(house);
% smoothed_blocks = lab2gaussfilt(blocks);
% [new_img, new_img2] = lab2sobelfilt(smoothed_house);
% [new_img, new_img2] = lab2sobelfilt(smoothed_blocks);
% 
% 
% sharpen_house = lab2sharpen(house, 5, 1); 
% sharpen_blocks = lab2sharpen(blocks, 5, 1); 
% [new_img, new_img2] = lab2sobelfilt(sharpen_house);
% [new_img, new_img2] = lab2sobelfilt(sharpen_blocks);

% % Sigma Filtering
new_img = lab2sigma(bridge, 30, 3);
% new_img = lab2gaussfilt(bridge);
% new_img = lab2sigma(bridge, 100, 3);

% % Takes time
% new_img = lab2sigma(jump, 30, 3);
% new_img = lab2gaussfilt(jump);
% new_img = lab2sigma(jump, 100, 3);




