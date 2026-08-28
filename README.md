# Average of a Numbered List

A Python program that accepts a space-separated list of heights, converts the input values into integers, calculates their total, and determines the average.

The final average is rounded to the nearest whole number before being displayed.

## Example

### Input

```text
Enter Height : 160 165 170 175 180
```

### Output

```text
5
The average height is 170
```

The first output represents the number of values entered.

## How It Works

The program processes the input through a sequence of simple steps:

```text
User Input
    ↓
Split into individual values
    ↓
Count the values
    ↓
Convert strings to integers
    ↓
Calculate the total
    ↓
Divide total by count
    ↓
Round the average
    ↓
Display result
```

## 1. Accepting the Input

The program receives the heights as a single string:

```python
height = input("Enter Height : ")
```

For example:

```text
160 165 170 175 180
```

## 2. Splitting the Input

The `split()` method separates the values:

```python
height_spilt = height.split()
```

The result is initially a list of strings:

```python
["160", "165", "170", "175", "180"]
```

## 3. Counting the Values

The program manually counts the number of elements:

```python
count = 0

for i in height_spilt:
    count += 1
```

For five entered heights:

```text
count = 5
```

## 4. Converting Strings to Integers

Input obtained through `input()` is stored as text.

The program converts each value into an integer:

```python
for y in range(count):
    height_spilt[y] = int(height_spilt[y])
```

The list changes from:

```python
["160", "165", "170", "175", "180"]
```

to:

```python
[160, 165, 170, 175, 180]
```

## 5. Calculating the Total

A running total is maintained:

```python
total = 0

for z in height_spilt:
    total += z
```

For the example:

```text
160 + 165 + 170 + 175 + 180 = 850
```

## 6. Finding the Average

The average is calculated using:

```python
avg = total / count
```

Therefore:

```text
850 / 5 = 170
```

The result is then rounded:

```python
round(avg)
```

## Implementation

```python
height = input("Enter Height : ")

height_spilt = height.split()

count = 0

for i in height_spilt:
    count += 1

print(count)

for y in range(count):
    height_spilt[y] = int(height_spilt[y])

total = 0

for z in height_spilt:
    total += z

avg = total / count

print("The average height is", round(avg))
```

## Example Walkthrough

Suppose the input is:

```text
150 160 170
```

After splitting:

```python
["150", "160", "170"]
```

After conversion:

```python
[150, 160, 170]
```

Count:

```text
3
```

Total:

```text
150 + 160 + 170 = 480
```

Average:

```text
480 / 3 = 160
```

Output:

```text
3
The average height is 160
```

## Complexity Analysis

Let `n` be the number of values entered.

| Metric | Complexity |
|---|---|
| Time Complexity | `O(n)` |
| Auxiliary Space | `O(n)` |

The program performs several passes over the list, but each pass is linear. Since multiple `O(n)` operations are still `O(n)` overall, the time complexity is `O(n)`.

The list containing the input values requires `O(n)` space.

## Concepts Covered

- `input()`
- `split()`
- Lists
- `for` loops
- Manual counting
- Type conversion with `int()`
- Running totals
- Arithmetic mean
- `round()`
- Basic list manipulation

## Important Detail

The values entered through `input()` initially exist as strings.

For example:

```python
height = "160 170 180"
```

After:

```python
height.split()
```

the values are still strings:

```python
["160", "170", "180"]
```

They must therefore be converted with `int()` before performing numerical addition.
