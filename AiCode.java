public static List<List<Integer>> getCoinCombinations(int amount) {
  List<List<Integer>> combinations = new ArrayList<>();
  int[] denominations = {1, 5, 10, 25};

  getCoinCombinationsRecursive(amount, denominations, new ArrayList<>(), combinations);

  return combinations;
}

private static void getCoinCombinationsRecursive(int amount, int[] denominations, List<Integer> currentCombination, List<List<Integer>> combinations) {
  if (amount == 0) {
    combinations.add(new ArrayList<>(currentCombination));
    return;
  }

  for (int denomination : denominations) {
    if (denomination <= amount) {
      currentCombination.add(denomination);
      getCoinCombinationsRecursive(amount - denomination, denominations, currentCombination, combinations);
      currentCombination.remove(currentCombination.size() - 1);
    }
  }
}
