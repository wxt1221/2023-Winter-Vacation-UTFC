## 排序评测题解


### LWF写作业
$~~~~~~$要动态地大块更改和随时排序，因为每次操作和上一次操作有关联，所以离线算法，每次更改完之后排一遍序不好，排序是针对任意序列的，但是更改后的序列具有一定的性质，虽然所有的数不一定满足单调性，但是假如将已更改和未更改的数分开看是一定具有单调性的，换句话说，也就是经过排序的，现在的问题就变成如何把这样两个单调序列合并成一个单调序列。而且在$O(n)$的时间复杂度中解决。

从最开始想，最终序列的第一个数，肯定是由两个序列中的第一个数决定的，从两个序列中的第一个数中选取最小的，放进新的序列，删掉原来的数，现在的两个序列仍是有序的，要求的除开已经放入答案后序列也是这两个删除已经加入答案的数后的序列合并而得，合并后的序列就放在答案序列的后面，同理可得，通过这样的方式一定可以在$O(n)$时间复杂度合并两个序列。

### YTC做题
$~~~~~~$原题要你求一个由$n$个数从$1$到$n$的排列$D$，求 $\sum^n_{i=1}(A_{C_i}-B_{D_i})^2$的最小值。

首先，可以确定 $C$ 对于答案是没有影响的，因为这个和只与元素的相对位置有关，所以可以把 $C$ 当做任意的$1$到$n$的排列。

$(A_{C_i}-B_{D_i})^2=(A_{C_i})^2+(B_{D_i})^2-2A_{C_i}B_{D_i}$

唯一有变化的是$-2A_{C_i}B_{D_i}$，要使他最大，换句话说就是$\sum^n_{i=1}A_{C_i}B_{D_i}$,最小。

引入排序不等式，在$A$和$B$有序的情况下，$C_i=D_i$，这个值最小，名为顺序和。

引入排序不等式，在$A$和$B$有序的情况下，$C_n-i+1=D_i$，也就是$D$是$C$经过反转得到的，这个值最小，名为逆序和。

其他的排列名为乱序和。

逆序和 $\leq$ 乱序和 $\leq$ 顺序和

关于这个公式的推理，比较复杂，https://b23.tv/0oiFfh2 可以去看一下，较为详细的讲解了这个定理的一种比较简单的推论。