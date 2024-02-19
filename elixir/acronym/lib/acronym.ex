defmodule Acronym do
  @doc """
  Generate an acronym from a string.
  "This is a string" => "TIAS"
  """
  @spec abbreviate(String.t()) :: String.t()
  def abbreviate(string) do
    string
    |> String.split(~r/\W+/)
    |> Enum.map(&String.upcase(&1))
    |> Enum.map(&String.slice(&1, 0))
    |> Enum.join()
  end
end
