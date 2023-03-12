defmodule NucleotideCount do
  @nucleotides MapSet.new [?A, ?C, ?G, ?T]

  @doc """
  Counts individual nucleotides in a DNA strand.

  ## Examples

  iex> NucleotideCount.count('AATAA', ?A)
  4

  iex> NucleotideCount.count('AATAA', ?T)
  1
  """
  @spec count(charlist(), char()) :: non_neg_integer()
  def count(strand, nucleotide) do
    Enum.count(strand, &(&1 == nucleotide))
  end

  @doc """
  Returns a summary of counts by nucleotide.

  ## Examples

  iex> NucleotideCount.histogram('AATAA')
  %{?A => 4, ?T => 1, ?C => 0, ?G => 0}
  """
  @spec histogram(charlist()) :: map()
  def histogram(strand) do
    initial = for n <- @nucleotides, into: %{}, do: {n, 0}
    strand
    |> Stream.filter(&MapSet.member?(@nucleotides, &1))
    |> Enum.reduce(initial, fn nucleotide, acc ->
      Map.update(acc, nucleotide, 1, &(&1 + 1))
    end)
  end
end
