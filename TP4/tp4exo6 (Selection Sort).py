def selection_sort(tab):
    n = len(tab)
    for i in range(n - 1):

        min_idx = i

        for j in range(i + 1, n):
            if tab[j] < tab[min_idx]:
                min_idx = j

        tab[i], tab[min_idx] = tab[min_idx], tab[i]
        print(tab)


def print_array(tab):
    for val in tab:
        print(val, end=" ")
    print()



tab = [64, 25, 12, 22, 11]

print(f"Selection Sort :\nOriginal array: ", end="")
print_array(tab)
print("-= Start Sorting =-")
selection_sort(tab)
print("-= Finish Sorting =-")
print("Sorted array: ", end="")
print_array(tab)

tab = [64, 25, 12, 22, 11]
print(f"\ntab.sort() :\nOriginal array: {tab}")
tab.sort()
print(f"Sorted array: {tab}")

tab = [64, 25, 12, 22, 11]
print(f"\nsorted(tab) :\nOriginal array: {tab}\nSorted array: {sorted(tab)}")






