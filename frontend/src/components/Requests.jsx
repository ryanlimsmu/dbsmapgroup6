import React from 'react'
import { useState } from 'react'
import Navbar from './requests/Navbar'
import Req_table from './requests/ReqTable'
import Alert_table from './requests/AlertTable'

const Requests = () => {

  const [requests, setRequests] = useState([
    {
        id: 1,
        request_date: "11/07/2020",
        company_name: "ABC",
        carbon_price: 11,
        carbon_qty: 13,
        requesting_reason: "ABCD",
        request_type: "Buy"
    }
  ])

  const [alert, setAlert] = useState(true)

  const toggleAlert = () => {
    setAlert(!alert)
  }

  const onAccept = (req_id) => {
    console.log('onAccept is clicked');
  }

  const onReject = (req_id) => {
    console.log('onReject is clicked');
  }

  const onAcceptAll = () => {
    const req_ids = [requests.map((req) => req.id)];
    console.log(req_ids);
  }

  const onRejectAll = () => {
    const req_ids = [requests.map((req) => req.id)];
    console.log('onRejectall is clicked');
  } 

  return (
    <div>
        <Navbar />
        {alert && <Alert_table alertRequests={ requests } toggleAlert={ toggleAlert } onAccept={onAccept} onReject={onReject} />} {/* To change */}
        <Req_table isHomePage={ false } requests={ requests } onAccept={onAccept} onReject={onReject} onAcceptAll={onAcceptAll} onRejectAll={onRejectAll}/>
    </div>
  )
}

export default Requests