function new_img = lab1locbox(img, window_size)

% Ensuring grey scale image
[row,col,ch] = size(img);

if(ch == 3)
    img = rgb2gray(img);
end

% % Borders pixel values are same with input image

% Necessary calculations in double format
data = double(img);
% new_img_data = data;
% 
% % Nested for loop for sliding window
% for i = window_size+1:row-window_size
%     for j = window_size+1:col-window_size
%         my_window = data((i-window_size):(i+window_size), (j-window_size):(j+window_size));
%         
%         mean_my_window = mean(my_window(:));
%         new_img_data(i, j) = mean_my_window;
%     end
% end
% new_img = uint8(new_img_data);
% 
% % Plots
% figure();
% subplot(2,1,1);
% imshow(img);
% title("Original Image");
% 
% subplot(2,1,2);
% imshow(new_img);
% title("Box Filtered Image, k = " + window_size);
% sgtitle('Leaving Borders as Original Values') 

% % FOR DIFFERENT APPROACHES UNCOMMENT THE BELOW PARTS

% % Borders pixel values are zero
new_img_data = zeros(row, col);
for i = window_size+1:row-window_size
    for j = window_size+1:col-window_size
        my_window = data((i-window_size):(i+window_size), (j-window_size):(j+window_size));
        
        mean_my_window = mean(my_window(:));
        new_img_data(i, j) = mean_my_window;
    end
end
new_img = uint8(new_img_data);

% figure();
% subplot(2,1,1);   
% imshow(img);
% title("Original Image");
% 
% subplot(2,1,2);
% imshow(new_img);
% title("Box Filtered Image, k = " + window_size);
% sgtitle('Borders as zero')
% 
% % % Borders are padded with zeros to make proper sliding window
% % Padding zeros to original data
% padded_data = zeros(row+2*window_size, col+2*window_size);
% [new_row, new_col] = size(padded_data);
% 
% data = double(img);
% padded_data(window_size+1:new_row-window_size, window_size+1:new_col-window_size) = data;
% 
% new_img_data = zeros(row, col);
% 
% for i = window_size+1:new_row-window_size
%     for j = window_size+1:new_col-window_size
%         my_window = padded_data((i-window_size):(i+window_size), (j-window_size):(j+window_size));
%         
%         mean_my_window = mean(my_window(:));
%         new_img_data(i-window_size, j-window_size) = mean_my_window;
%     end
% end
% 
% new_img = uint8(new_img_data);
% 
% figure();
% subplot(2,1,1);
% imshow(img);
% title("Original Image");
% 
% subplot(2,1,2);
% imshow(new_img);
% title("Box Filtered Image, k = " + window_size);
% sgtitle('Borders are zero padded')

end














