import React from 'react'
import "../../css/ReqTable.css"
import ReqButtons from "./ReqButtons"

const AlertTable = ({ alertRequests, toggleAlert, onAccept, onReject }) => {
  return (
    <div className='container'>
        <button type="button" onClick={() => toggleAlert()}>x</button>
        <table>
        <tr>
          <th>Request date</th>
          <th>Requester Company Name</th>
          <th>Carbon Price</th>
          <th>Carbon Quantity</th>
          <th>Requesting Reason</th>
          <th>Request Type</th>
          <th>Action</th>
        </tr>
      <tbody>
        {alertRequests.map((req) => ( 
          <tr>
            <td>{req.request_date}</td>
            <td>{req.company_name}</td>
            <td>{req.carbon_price}</td>
            <td>{req.carbon_qty}</td>
            <td>{req.requesting_reason}</td>
            <td>{req.request_type}</td>
            <td>{<ReqButtons onAccept={onAccept} onReject={onReject} req_id={req.id}/>}</td>
          </tr>
          ))}
      </tbody>
     </table>
    </div>
  )
}

export default AlertTable