defmodule GuessingGame do
  def compare(secret_number, guess \\ :no_guess) do
    cond do
      guess == :no_guess -> "Make a guess"
      secret_number == guess -> "Correct"
      abs(secret_number - guess) == 1 -> "So close"
      guess > secret_number -> "Too high"
      true -> "Too low"
    end
  end
end
