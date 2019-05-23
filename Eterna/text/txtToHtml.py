import glob
import os.path


files = glob.glob('*.txt') #// 특정확장자를 가진 목록뽑기
for x in files:#
    if not os.path.isdir(x): #// 파일만 걸러내기
        filename = os.path.splitext(x)# // 확장자와 순수파일명 구분하기
        print (filename[0]) #// 확인 주석
        os.rename(x, filename[0]  + '.html') #// 순수파일명에 gz확장자 붙이기
