function new_img = lab1condscale(img, ref_img)

[row,col,ch] = size(img); 

[row2,col2,ch2] = size(ref_img);

if(ch == 3)
    img = rgb2gray(img);
end

if(ch2 == 3)
    ref_img = rgb2gray(ref_img);
end

data_I = double(ref_img);
mean_I = mean(data_I(:));
std_I = std(data_I(:));

data_J = double(img);
mean_J = mean(data_J(:));
std_J = std(data_J(:));

a = (mean_I * (std_J / std_I)) - mean_J;

b = std_I / std_J;

new_img_data = b * (data_J + a);
new_img = uint8(new_img_data);

mean_new_img = mean(new_img_data(:));
std_new_img = std(new_img_data(:));

figure();
subplot(2,2, [1:2]);
imshow(ref_img);
title("Reference Image");
xlabel({"Mean = " + mean_I ; "Std = " + std_I});

subplot(2,2,3);
imshow(img);
title("Current Image");
xlabel({"Mean = " + mean_J ; "Std = " + std_J});

subplot(2,2,4);
imshow(new_img);
title("Resulting Image");
xlabel({"Mean = " + mean_new_img ; "Std = " + std_new_img});

end