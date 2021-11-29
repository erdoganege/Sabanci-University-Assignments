function [new_img, cornerlist] = lab4ktcorners(img, threshold, k)

% Ensuring grey scale image
[row,col,ch] = size(img);
if(ch == 3)
    img = rgb2gray(img);
end


new_img = imgaussfilt(img);
data = double(new_img);

[Gx, Gy] = imgradientxy(data);
cornerlist = [];
for i = k+1:row-k 
    for j = k+1:col-k
        my_window = Gx((i-k):(i+k), (j-k):(j+k));
        my_window2 = Gy((i-k):(i+k), (j-k):(j+k));
        IX = sum(sum(my_window.*my_window));
        IY = sum(sum(my_window2.*my_window2));
        IXY = sum(sum(my_window.*my_window2));
        
        H = [IX, IXY; IXY, IY];
        values = eig(H);

        if min(values) > threshold
            cornerlist = [cornerlist; [i,j]];
        end
    end
end



