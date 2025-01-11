import React from 'react'

const ReqButtons = ({ onAccept, onReject, req_id }) => {
  return (
    <div>
        <button style={{ backgroundColor: 'green', marginRight: '10px' }} onClick={() => onAccept(req_id)} type='button'>Accept</button>
        <button style={{ backgroundColor: 'red' }} onClick={() => onReject(req_id)} type='button'>Reject</button>
    </div>
  )
}

export default ReqButtons