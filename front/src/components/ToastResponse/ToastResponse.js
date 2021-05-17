import React, { useContext } from "react";
import { Toast } from "react-bootstrap";
import AppContext from "../../context/AppContext";

function ToastResponse() {
  const appContext = useContext(AppContext);
  const { setShowToast, showToast, toastMessage, toastStatus } = appContext;

  return (
    <Toast
      className={`toast-fixed bg-${toastStatus}`}
      onClose={() => setShowToast(false)}
      show={showToast}
      delay={3000}
      autohide
    >
      <Toast.Header>
        <span className="mr-auto">{toastMessage}</span>
      </Toast.Header>
    </Toast>
  );
}

export default ToastResponse;
