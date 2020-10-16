import React, { useEffect, useRef } from 'react';
import styled from 'styled-components';
import Message, { MessageInterface } from './message/message';
import Scrollbar from '../scrollbar/scrollbar';

const StyledMessages = styled.div`
  display: flex;
  flex-flow: column;
  background: ${({ theme }) => theme.bg};
  color: ${({ theme }) => theme.fg};
  width: 100%;
  height: 100%;
`;

export interface MessagesInterface {
  messages: MessageInterface[];
}

const Messages: React.FC<MessagesInterface> = ({
  messages,
}) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: 'smooth',
    });
  }, [messages]);

  return (
    <StyledMessages>
      <Scrollbar>
        {messages.map(({ name, message }, index) => <Message key={index} name={name} message={message}/>)}
        <div ref={messagesEndRef} />
      </Scrollbar>
    </StyledMessages>
  );
};

export default Messages;
