/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
C#, VB, Perl, Swift, Prolog, Javascript, Pascal, HTML, CSS, JS
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
int main()
{
 int a1[50],a2[50],r[100],m,n,i,j,k;
 printf("enter the size of first array:");
 scanf("%d",&m);
 printf("enter the sorted elements of first array:");
 for(i=0;i<m;i++)
 scanf("%d",&a1[i]);
 printf("enter the size of second array:");
 scanf("%d",&n);
 printf("enter the sorted elements of second array:");
 for(i=0;i<n;i++)
 scanf("%d",&a2[i]);
 i=j=k=0;
 while(i<m&&j<n)
 {
 if(a1[i]<a2[j])
 {
 r[k]=a1[i];
 i++;
 k++;
 }
 else
 {
 r[k]=a2[j];
 j++;
 k++;
 }
 }
 while(i<m)
 {
 r[k]=a1[i];
 i++;
 k++;

 }
 while(j<n)
 {

 r[k]=a2[j];
 j++;
 k++;
 }
 printf("\nElements in first array:");
 for(i=0;i<m;i++)
 {
 printf(" %d",a1[i]);
 }
 printf("\nElements in second array:");
 for(i=0;i<n;i++)
 {
 printf(" %d",a2[i]);
 }
 printf("\nMerged array is:");
 for(i=0;i<m+n;i++)
 {
 printf(" %d",r[i]);
 }
 return 0;
}