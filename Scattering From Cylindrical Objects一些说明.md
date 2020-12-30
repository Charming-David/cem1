# Scattering From Cylindrical Objects

### 定义电导率磁导率区域

![image-20201230162855494](C:\Users\David Lyu\AppData\Roaming\Typora\typora-user-images\image-20201230162855494.png)入射场epsilon（mu也是相同的）



![image-20201230162858732](C:\Users\David Lyu\AppData\Roaming\Typora\typora-user-images\image-20201230162858732.png)散射场epsilon

![image-20201230163034926](C:\Users\David Lyu\AppData\Roaming\Typora\typora-user-images\image-20201230163034926.png)入射场sigma（保证周围有一圈PML）

![image-20201230163112713](C:\Users\David Lyu\AppData\Roaming\Typora\typora-user-images\image-20201230163112713.png)散射场sigma（不仅考虑圆柱体的sigma也要考虑PML）

### 迭代公式的跟新

![9C13C516BCAB64C7B78E0A0263071D90](C:\Users\David Lyu\Documents\Tencent Files\1311576307\FileRecv\MobileFile\9C13C516BCAB64C7B78E0A0263071D90.png)

在TFSF的迭代公式（上式）内引入PML，情况与入射场的类似，只需要sigma和sigma_m满足阻抗匹配的关系即可。但是在PML层内需要屏蔽掉入射场的影响，因为这种情况下中括号内不等于0（有sigma和sigma_m）。程序里面让中括号乘以一个系数alpha，在PML区域内等于0就可以，这就保证散射场的行为就是一个正常的传播的场入射到PML。