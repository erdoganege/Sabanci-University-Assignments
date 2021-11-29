function [new_img, cornerlist] = lab4Harriscorners(img, threshold, k)

% Ensuring grey scale image
[row,col,ch] = size(img);
if(ch == 3)
    img = rgb2gray(img);
end

new_img = imgaussfilt(img);
data = double(new_img);

[Gx, Gy] = imgradientxy(data);
cornerlist = [];
for i = k+1:row-k %Edges are zero
    for j = k+1:col-k
        my_window = Gx((i-k):(i+k), (j-k):(j+k));
        my_window2 = Gy((i-k):(i+k), (j-k):(j+k));
        IX = sum(sum(my_window.*my_window));
        IY = sum(sum(my_window2.*my_window2));
        IXY = sum(sum(my_window.*my_window2));
        
        H = [IX, IXY; IXY, IY];
        my_det = (H(1,1)*H(2,2)) - (H(1,2) * H(2, 1));
        trace = H(1,1) + H(2,2);
        f = my_det / trace;     
        if f > threshold
            cornerlist = [cornerlist; [i,j]];
        end
    end
end
