% blocks = imread("blocks.png");
% monastry = imread("Monastry.bmp");
% MY_checkerboard = checkerboard(40);
% house = imread("house.png");
% 
% % % % % PART 1 
k = 1;
[new_img, cornerlist] = lab4ktcorners(blocks, 50000, k);

figure();
subplot(1,3,1)
imshow(new_img);
title("Threshold: "+ 50000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
hold on
if size(cornerlist)[0] ~= 0;
    plot(cornerlist(:,2), cornerlist(:,1),'r*')
end
[new_img, cornerlist] = lab4ktcorners(monastry, 50000, k);
subplot(1,3,2)
imshow(new_img);
title("Threshold: "+ 50000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
hold on
if size(cornerlist)[0] ~= 0;
    plot(cornerlist(:,2), cornerlist(:,1),'r*')
end
[new_img, cornerlist] = lab4ktcorners(MY_checkerboard, 10, k);
subplot(1,3,3)
imshow(MY_checkerboard);
title("Threshold: "+ 10 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
hold on
if size(cornerlist)[0] ~= 0;
    plot(cornerlist(:,2), cornerlist(:,1),'r*')
end
sgtitle('Kanade-Tomasi Algorithm for Corner Detection')


% 
% % % Harris with f PART 2 
k = 1;
[new_img, cornerlist] = lab4Harriscorners(blocks, 50000, k);
figure();
subplot(1,3,1)
imshow(new_img);
title("Threshold: "+ 50000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
hold on
if size(cornerlist)[0] ~= 0;
    plot(cornerlist(:,2), cornerlist(:,1),'r*')
end

[new_img, cornerlist] = lab4Harriscorners(monastry, 50000, k);
subplot(1,3,2)
imshow(new_img);
title("Threshold: "+ 50000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
hold on
if size(cornerlist)[0] ~= 0;
    plot(cornerlist(:,2), cornerlist(:,1),'r*')
end

[new_img, cornerlist] = lab4Harriscorners(MY_checkerboard, 5, k);
subplot(1,3,3)
imshow(MY_checkerboard);
title("Threshold: "+ 5 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
hold on
if size(cornerlist)[0] ~= 0;
    plot(cornerlist(:,2), cornerlist(:,1),'r*')
end
sgtitle('Harris with f Algorithm for Corner Detection')

% 
% % % % Harris with R PART 3
k = 1;
[new_img, cornerlist] = lab4Harriscorners_R(blocks, 10^9, k);
figure();
subplot(1,3,1)
imshow(new_img);
title("Threshold: "+ 10^9 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
hold on
if size(cornerlist)[0] ~= 0;
    plot(cornerlist(:,2), cornerlist(:,1),'r*')
end

[new_img, cornerlist] = lab4Harriscorners_R(monastry, 10^9, k);
subplot(1,3,2)
imshow(new_img);
title("Threshold: "+ 10^9 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
hold on
if size(cornerlist)[0] ~= 0;
    plot(cornerlist(:,2), cornerlist(:,1),'r*')
end

[new_img, cornerlist] = lab4Harriscorners_R(MY_checkerboard, 10, k);
subplot(1,3,3)
imshow(MY_checkerboard);
title("Threshold: "+ 10 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
hold on
if size(cornerlist)[0] ~= 0;
    plot(cornerlist(:,2), cornerlist(:,1),'r*')
end
sgtitle('Harris with R Algorithm for Corner Detection')




% % % % % Kanade-Tomasi Other Examples
% k = 1;
% [new_img, cornerlist] = lab4ktcorners(blocks, 20000, k);
% 
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 20000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% [new_img, cornerlist] = lab4ktcorners(monastry, 20000, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 20000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% [new_img, cornerlist] = lab4ktcorners(MY_checkerboard, 2, k);
% subplot(1,3,3)
% imshow(MY_checkerboard);
% title("Threshold: "+ 2 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Kanade-Tomasi Algorithm for Corner Detection')
% 
% 
% k = 1;
% [new_img, cornerlist] = lab4ktcorners(blocks, 100000, k);
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 100000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4ktcorners(monastry, 100000, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 100000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4ktcorners(MY_checkerboard, 20, k);
% subplot(1,3,3)
% imshow(MY_checkerboard);
% title("Threshold: "+ 20 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Kanade-Tomasi Algorithm for Corner Detection')
% 
% k = 3;
% [new_img, cornerlist] = lab4ktcorners(blocks, 100000, k);
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 100000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4ktcorners(monastry, 100000, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 100000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4ktcorners(MY_checkerboard, 20, k);
% subplot(1,3,3)
% imshow(MY_checkerboard);
% title("Threshold: "+ 20 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Kanade-Tomasi Algorithm for Corner Detection')
% 
% k = 1;
% [new_img, cornerlist] = lab4ktcorners(house, 10000, k);
% 
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 10000 + " Window Size: " + (2*k+1) + "x"+ (2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% [new_img, cornerlist] = lab4ktcorners(house, 50000, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 50000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% [new_img, cornerlist] = lab4ktcorners(house, 100000, k);
% subplot(1,3,3)
% imshow(new_img);
% title("Threshold: "+ 100000 + " Window Size: " + (2*k+1) + "x"+ (2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Kanade-Tomasi Algorithm for Corner Detection')
% % 
% % % % % Harris Algorithm with f Other Examples
% % % 
% k = 1;
% [new_img, cornerlist] = lab4Harriscorners(blocks, 20000, k);
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 20000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners(monastry, 20000, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 20000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners(MY_checkerboard, 2, k);
% subplot(1,3,3)
% imshow(MY_checkerboard);
% title("Threshold: "+ 2 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Harris with f Algorithm for Corner Detection')
% % 
% k = 1;
% [new_img, cornerlist] = lab4Harriscorners(blocks, 100000, k);
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 100000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners(monastry, 100000, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 100000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners(MY_checkerboard, 20, k);
% subplot(1,3,3)
% imshow(MY_checkerboard);
% title("Threshold: "+ 20 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Harris with f Algorithm for Corner Detection')
% % 
% k = 3;
% [new_img, cornerlist] = lab4Harriscorners(blocks, 100000, k);
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 100000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners(monastry, 100000, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 100000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners(MY_checkerboard, 20, k);
% subplot(1,3,3)
% imshow(MY_checkerboard);
% title("Threshold: "+ 20 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Harris with f Algorithm for Corner Detection')
% 
% k = 1;
% [new_img, cornerlist] = lab4Harriscorners(house, 10000, k);
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 10000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners(house, 50000, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 50000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners(house, 100000, k);
% subplot(1,3,3)
% imshow(new_img);
% title("Threshold: "+ 100000 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Harris with f Algorithm for Corner Detection')
% 
% % 
% % 
% % % % Harris Algorithm with R Other Examples
% k = 1;
% [new_img, cornerlist] = lab4Harriscorners_R(blocks, 10^6, k);
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 10^6 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners_R(monastry, 10^6, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 10^6 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners_R(MY_checkerboard, 5, k);
% subplot(1,3,3)
% imshow(MY_checkerboard);
% title("Threshold: "+ 5 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Harris with R Algorithm for Corner Detection')
% % 
% k = 1;
% [new_img, cornerlist] = lab4Harriscorners_R(blocks, 10^10, k);
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 10^10 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners_R(monastry, 10^10, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 10^10 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners_R(MY_checkerboard, 20, k);
% subplot(1,3,3)
% imshow(MY_checkerboard);
% title("Threshold: "+ 20 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Harris with R Algorithm for Corner Detection')
% % 
% k = 3;
% [new_img, cornerlist] = lab4Harriscorners_R(blocks, 10^10, k);
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 10^10 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners_R(monastry, 10^10, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 10^10 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners_R(MY_checkerboard, 20, k);
% subplot(1,3,3)
% imshow(MY_checkerboard);
% title("Threshold: "+ 20 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Harris with R Algorithm for Corner Detection')
% 
% k = 1;
% [new_img, cornerlist] = lab4Harriscorners_R(house, 10^9, k);
% figure();
% subplot(1,3,1)
% imshow(new_img);
% title("Threshold: "+ 10^9 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners_R(house, 10^10, k);
% subplot(1,3,2)
% imshow(new_img);
% title("Threshold: "+ 10^10 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% 
% [new_img, cornerlist] = lab4Harriscorners_R(house, 10^11, k);
% subplot(1,3,3)
% imshow(new_img);
% title("Threshold: "+ 10^11 + " Window Size: " + (2*k+1) + "x"+(2*k+1))
% hold on
% if size(cornerlist)[0] ~= 0;
%     plot(cornerlist(:,2), cornerlist(:,1),'r*')
% end
% sgtitle('Harris with R Algorithm for Corner Detection')


% % Compare Harris with different functions
% k = 1;
% tStart1 = tic;  
% [new_img, cornerlist] = lab4Harriscorners_R(house, 10^9, k);
% tEnd1 = toc(tStart1)
% 
% tStart2 = tic;  
% [new_img, cornerlist] = lab4Harriscorners(house, 10^9, k);
% tEnd2 = toc(tStart2)

% % Compare Harris and Kanade-Tomasi
% k = 1;
% tStart1 = tic;  
% [new_img, cornerlist1] = lab4ktcorners(house, 10^9, k);
% tEnd1 = toc(tStart1)
% 
% tStart2 = tic;  
% [new_img, cornerlist2] = lab4Harriscorners(house, 10^9, k);
% tEnd2 = toc(tStart2)
% 
% tStart3 = tic;  
% [new_img, cornerlist3] = lab4Harriscorners_R(house, 10^9, k);
% tEnd3 = toc(tStart3)


% figHandles = findall(0,'Type','figure');
% temp = size(figHandles);
% for i = temp(1):-1:1
% path = "C:\Users\user\Desktop\erdoganege_EE417_POSTLAB4\figure" +i;
% saveas(figHandles(i),path);
% end






