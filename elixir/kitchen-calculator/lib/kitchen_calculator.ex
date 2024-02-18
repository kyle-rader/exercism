defmodule KitchenCalculator do
  def get_volume(volume_pair) do
    {unit, volume} = volume_pair
    volume
  end

  def to_milliliter(volume_pair) do
    # Please implement the to_milliliter/1 functions
    case {unit, volume} = volume_pair do
      {:milliliter, volume} -> {:milliliter, volume }
      {:cup, volume} -> {:milliliter, volume * 240 }
      {:fluid_ounce, volume} -> {:milliliter, volume * 30 }
      {:tablespoon, volume} -> {:milliliter, volume * 15 }
      {:teaspoon, volume} -> {:milliliter, volume * 5 }
    end
  end

  def from_milliliter(volume_pair, unit) do
    # Please implement the from_milliliter/2 functions
    vol = get_volume(volume_pair)

    case {unit, vol} do
      {:milliliter, volume} -> {unit, volume}
      {:liter, volume} -> {unit, volume / 1000}
      {:cup, volume} -> {unit, volume / 240}
      {:fluid_ounce, volume} -> {unit, volume / 30}
      {:tablespoon, volume} -> {unit, volume / 15}
      {:teaspoon, volume} -> {unit, volume / 5}
      {unsupported_unit, vol} -> raise "Unknown unit #{unsupported_unit}"
    end
  end

  def convert(volume_pair, unit) do
    # Please implement the convert/2 function
    volume_pair
      |> to_milliliter()
      |> from_milliliter(unit)
  end
end
