# Longest Increasing Subsequence Length Program

def lis_length(numbers):
  n = len(numbers)
  if n == 0:
    return 0

  # dp[i] = length of LIS ending at index i
  dp = [1] * n

  for i in range(n):
    for j in range(i):
      if numbers[j] < numbers[i]:
        dp[i] = max(dp[i], dp[j] + 1)

  # The answer is the maximum of all dp values
  return max(dp)


def main():
  # Read numbers from user as space-separated values
  raw = input("Enter numbers separated by space: ").strip()

  if raw == "":
    print("No input provided.")
    return

  parts = raw.split()
  numbers = []

  for p in parts:
    try:
      numbers.append(int(p))
    except ValueError:
      print(f"Skipping invalid value: {p}")

  if not numbers:
    print("No valid numbers to process.")
    return

  result = lis_length(numbers)
  print("Length of Longest Increasing Subsequence:", result)


if __name__ == "__main__":
  main()
