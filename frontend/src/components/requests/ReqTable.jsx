import React from 'react'
import '../../css/ReqTable.css'
import ReqButtons from './ReqButtons'
import HomeButton from './HomeButton'

const ReqTable = ( { isHomePage, requests, onAccept, onReject, onAcceptAll, onRejectAll } ) => {
  return (
    <div className='container'>
      <table>
        <tr>
          <th>Request date</th>
          <th>{ !isHomePage ? "Requester Company Name" : "Company Name"}</th>
          <th>Carbon Price</th>
          <th>Carbon Quantity</th>
          <th>Requesting Reason</th>
          <th>Request Type</th>
          <th>Action</th>
        </tr>
      <tbody>
        {requests.map((req) => ( 
          <tr>
            <td>{req.request_date}</td>
            <td>{req.company_name}</td>
            <td>{req.carbon_price}</td>
            <td>{req.carbon_qty}</td>
            <td>{req.requesting_reason}</td>
            <td>{req.request_type}</td>
            <td>{ isHomePage ? <HomeButton /> : <ReqButtons onAccept={onAccept} onReject={onReject} req_id={req.id}/> }</td>
          </tr>
          ))}
      </tbody>
    </table>
    <div style={{ display: 'inline' }}>
      <button type='button' onClick={onAcceptAll}>Accept All</button>
      <button type='button' onClick={onRejectAll}>Reject All</button>
    </div>
   </div>
  )
}

export default ReqTable