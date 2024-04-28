import { useState } from "react";

export default function FilterForm() {
  const [filter, setFilter] = useState({
    trailLength: 0,
    trailTranspDist: 0,
    transport: { bus: false, train: false, other: false, all: false },
  });

  const handleClick = (key, value) => {
    const updatedTransport = { ...filter.transport, [key]: value };
    setFilter({ ...filter, transport: updatedTransport });
  };

  return (
    <form>
      <label>
        Trail length:
        <input
          type="number"
          onBlur={(e) => setFilter({ ...filter, trailLength: e.target.value })}
        />
      </label>
      <br />
      <label>
        Trail distance from public transport stop:
        <input
          type="number"
          onBlur={(e) => setFilter({ ...filter, trailTranspDist: e.target.value })}
        />
      </label>
      <br />
      <label>
        Transport mode:
        <br />
        <input
          type="checkbox"
          name="checkbox1"
          onClick={(e) => handleClick("bus", e.target.checked)}
        />
        Bus
        <br />
        <input
          type="checkbox"
          name="checkbox2"
          onClick={(e) => handleClick("train", e.target.checked)}
        />
        Train
        <br />
        <input
          type="checkbox"
          name="checkbox3"
          onClick={(e) => handleClick("other", e.target.checked)}
        />
        Other
        <br />
        <input
          type="checkbox"
          name="checkbox4"
          onClick={(e) => handleClick("all", e.target.checked)}
        />
        All
      </label>
    </form>
  );
}
