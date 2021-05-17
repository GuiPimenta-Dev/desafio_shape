import React, { useContext, useState } from "react";
import { Card, ListGroup, Form, Button } from "react-bootstrap";
import AppContext from "../../context/AppContext";

function ListVessels() {
  const [vesselCode, setVesselCode] = useState("");
  const appContext = useContext(AppContext);
  const { handleFind, equipmentsList } = appContext;

  const handleFindButton = () => {
    if (vesselCode) {
      handleFind(vesselCode);
      setVesselCode("");
    }
  };

  const handleInput = (e) => {
    setVesselCode(e.target.value);
  };

  return (
    <Card className="p-3 mt-3">
      <Form>
        <Form.Group controlId="formBasicEmail">
          <Form.Label>Return all active equipment of a vessel:</Form.Label>
          <div className="d-flex">
            <Form.Control
              onChange={handleInput}
              value={vesselCode}
              className="mr-2"
              type="text"
              placeholder="Vessel Code"
            />
            <Button onClick={handleFindButton} variant="info">
              Find
            </Button>
          </div>
        </Form.Group>
      </Form>

      <ListGroup variant="flush" className="box overflow-auto">
        {equipmentsList.map((equip) => (
          <ListGroup.Item
            className="text-center"
            key={equip.code}
          >{`${equip.code} | ${equip.name} | ${equip.location} | ${equip.status}`}</ListGroup.Item>
        ))}
      </ListGroup>
    </Card>
  );
}
export default ListVessels;
