clear all
close all
clc
%%
% this is a sample code to study the retinal images

%read image
A = imread('C:\Users\arunsaranathhome\Downloads\KaggleCompetition\sample\10close all_left.jpeg','jpeg');

figure()
subplot(2,2,1)
imagesc(A)
 colormap('gray')
title('Original Image')
subplot(2,2,2)
imagesc(squeeze(A(:,:,1)))
 colormap('gray')
title('R-Band')
subplot(2,2,3)
imagesc(squeeze(A(:,:,2)))
 colormap('gray')
title('G-Band')
subplot(2,2,4)
imagesc(squeeze(A(:,:,3)))
 colormap('gray')
 title('B-Band')
%  %%
%  %EDGE DETECTION - FAIL
%  BW1 = edge(squeeze(A(:,:,2)),'sobel');
% BW2 = edge(squeeze(A(:,:,2)),'canny');
% figure;
% imshowpair(BW1,BW2,'montage')
% title('Sobel Filter                                   Canny Filter');
%%
AA  = squeeze(A(:,:,1));
AA(AA>40)=1;
BW1 = edge(AA,'canny');
%%
figure()
imagesc(BW1)
title('retina edge')
