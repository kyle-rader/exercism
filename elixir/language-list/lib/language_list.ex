defmodule LanguageList do
  @elixir "Elixir"

  def new(), do: []
  def add(list, language), do: [language | list]
  def remove([_ | rest]), do: rest
  def first([first | _]), do: first
  def count(list), do: length(list)
  def functional_list?(list), do: list |> Enum.any?(&(&1 == @elixir))
end
