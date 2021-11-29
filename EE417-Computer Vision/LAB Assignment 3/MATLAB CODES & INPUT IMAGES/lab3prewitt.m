function new_img_Edges = lab3prewitt(img, threshold)

% Ensuring grey scale image
[row,col,ch] = size(img);
if(ch == 3)
    img = rgb2gray(img);
end

x_filter = [-1,0,1; -1,0,1; -1,0,1];

y_filter = [-1,-1,-1; 0,0,0; 1,1,1];

data = double(img);
% % Double for loop for sliding window
new_img_data_X = zeros(row, col);
new_img_data_Y = zeros(row, col);
window_size = 1;
for i = window_size+1:row-window_size %Edges are zero
    for j = window_size+1:col-window_size
        my_window = data((i-window_size):(i+window_size), (j-window_size):(j+window_size)); %take the window
        value_X = sum(sum(my_window .* x_filter)); %Convolution operation
        value_Y = sum(sum(my_window .* y_filter)); %Convolution operation
        
        new_img_data_X(i, j) = value_X;
        new_img_data_Y(i, j) = value_Y;
    end
end
new_img_X = uint8(new_img_data_X);  %Prewitt X filtered image
new_img_Y = uint8(new_img_data_Y);  %Prewitt Y filtered image

new_img_data_G = sqrt(new_img_data_X.^2 + new_img_data_Y.^2); %applying formula
new_img_G = uint8(new_img_data_G);

[row2,col2,ch2] = size(new_img_data_G);
new_img_data_Edges = zeros(row2,col2); 

indexes = find(new_img_data_G>threshold); %indexes with higher values than threshold

new_img_data_Edges = reshape(new_img_data_Edges, [row2*col2, 1]);
new_img_data_Edges(indexes) = 255; %make them white
new_img_data_Edges = reshape(new_img_data_Edges, [row2, col2]);
% for i = 1:row2
%     for k = 1:col2
%         if new_img_data_G(i, k) > threshold
%             new_img_data_Edges(i, k) = 255;
%         end
%     end
% end
new_img_Edges = uint8(new_img_data_Edges);

% Plots
figure();
subplot(3,3,1);
imshow(img);
title("Original Image");

subplot(3,3,2);
imshow(new_img_X);
title("Prewitt X Filtered Image");

subplot(3,3,3);
imshow(new_img_Y);
title("Prewitt Y Filtered Image");

subplot(3,3,5);
imshow(new_img_G);
title("Prewitt Gradient");

subplot(3,3,6);
imshow(new_img_Edges);
title("Prewitt Edges with threshold " + threshold);




