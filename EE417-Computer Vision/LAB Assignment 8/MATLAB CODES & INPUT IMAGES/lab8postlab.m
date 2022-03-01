left = imread("S01L.png");
right = imread("S01R.png");
left = rgb2gray(left);
right = rgb2gray(right);

% % To see with following images uncomment below lines and comment upper 4
% left = imread("S00L.tif");
% right = imread("S00R.tif");
% left = rgb2gray(left);
% right = rgb2gray(right);

k = 10;
w1 = 60;
w2 = 0;
[row, col, ch] = size(left);
paddedleft = padarray(left, [k+w1+w2 k+w1+w2], "both");
paddedright = padarray(right, [k+w1+w2 k+w2+w1], "both");

data_left = double(paddedleft);
data_right = double(paddedright);

[padded_row,padded_col,ch] = size(paddedleft);
dispar1 = zeros(padded_row,padded_col);

for i = k+w1+w2+1:row+k+w1+w2
    for j = k+w1+w2+1:col+k+w1+w2
        left_window = data_left((i-k):(i+k), (j-k):(j+k));
        dist = [];
        for m = 1:w1
            for m2 = 0:w2
            right_window = data_right((i-k-m2):(i+k-m2), (j-k-m):(j+k-m));
            diff = left_window - right_window;
            square = diff.*diff;
            result = sum(sum(square));
            dist = [dist; [m m2 result]];
            end
        end
        ind = find(dist(:,3) == min(dist(:,3)));
        dispar1(i, j) = dist(ind(1), 1);
    end
end
% dispar1 = uint8(dispar1);
figure();
imshow(stereoAnaglyph(left,right));
title("Stereo Anaglyph");
figure; imagesc(dispar1); colormap jet; colorbar
title("k = "+k + " w1 = " + w1 + " w2 = " + w2);


% % Disparity Map with built-in function for S01 images
disparityRange = [0 64];
disparityMap = disparityBM(left, right,'DisparityRange',disparityRange);
figure();
imshow(disparityMap,disparityRange);
title('Disparity Map with Built-in Function');
colormap(gca,jet) 
colorbar


% % Disparity Map with built-in function for S00 images
% disparityRange = [0 48];
% disparityMap = disparityBM(left, right,'DisparityRange',disparityRange);
% figure();
% imshow(disparityMap,disparityRange);
% title('Disparity Map with Built-in Function');
% colormap(gca,jet) 
% colorbar
