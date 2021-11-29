function med = myMedian (img)

[row,col,ch] = size (img);
Card = row*col;
if (ch==3)
    img = rgb2gray(img);
end

Data = reshape(img, [1, Card]);

Sorted = sort(Data);

if mod(Card, 2) == 0
    ind = Card / 2;
    med = (Sorted(ind) + Sorted(ind + 1)) / 2;
else
    ind = (Card + 1) / 2;
    med = Sorted(ind);
end
end
    