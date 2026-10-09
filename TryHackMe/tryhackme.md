# Catatan TryHackMe: Introduction to Python

## Task 1: Introduction to Python
Materi pengenalan Python.

## Task 2: Hello World

**Kode:**
```python
print("Hello World")
```

**Flag:** `THM{PRINT_STATEMENTS}`

## Task 3: Mathematical Operators

| Operasi | Kode | Flag |
|---|---|---|
| Penjumlahan | `print(21 + 43)` | `THM{ADDITI0N}` |
| Pengurangan | `print(142 - 52)` | `THM{SUBTRCT}` |
| Perkalian | `print(10 * 342)` | `THM{MULTIPLICATION_PYTHON}` |
| Pangkat | `print(5 ** 2)` | `THM{EXP0N3NT_POWER}` |

## Task 4: Variables and Data Types

**Kode:**
```python
height = 200
height = height + 50
print(height)
```

**Flag:** `THM{VARIABL3S}`

## Task 5: Logical and Boolean Operators

Belum ada kode atau flag yang dicatat.

## Task 6: Shipping Project — Introduction to If Statements

### Soal 1: Biaya pengiriman dengan nilai awal

**Kode:**
```python
customer_basket_cost = 34
customer_basket_weight = 44

if customer_basket_cost > 100:
    shipping_cost = 0
else:
    shipping_cost = customer_basket_weight * 1.20

total_cost = customer_basket_cost + shipping_cost

print(total_cost)
```

**Flag:** `THM{IF_STATEMENT_SHOPPING}`

### Soal 2: Biaya pengiriman saat belanja $101

**Kode:**
```python
customer_basket_cost = 101
customer_basket_weight = 44

if customer_basket_cost > 100:
    shipping_cost = 0
else:
    shipping_cost = customer_basket_weight * 1.20

total_cost = customer_basket_cost + shipping_cost

print(total_cost)
```

**Flag:** `THM{MY_FIRST_APP}`

## Task 7: Loops

**Kode:**
```python
for i in range(51):
    print(i)
```

**Flag:** `THM{L00PS_WHILE_FOR}`

## Task 8: Bitcoin Project — Introduction to Functions

**Kode:**
```python
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    usd_value = bitcoin_amount * bitcoin_value_usd
    return usd_value

bitcoin_amount = 1.2
bitcoin_to_usd = 30000

investment_value = bitcoinToUSD(bitcoin_amount, bitcoin_to_usd)

if investment_value < 30000:
    print("Bitcoin investment is below $30,000!")
else:
    print("Bitcoin investment is at least $30,000.")
```

**Flag:** `THM{BITC0IN_INVESTOR}`

## Task 9: Files

**Kode:**
```python
f = open("flag.txt", "r")
print(f.read())
f.close()
```

**Flag:** `THM{F1LE_R3AD}`

## Task 10: Imports
