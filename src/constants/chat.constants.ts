import { MessageInterface } from '../components/messages/message/message';

export interface ChatStateInterface {
  messages: MessageInterface[];
}

export const CHAT_INITIAL_STATE: ChatStateInterface = {
  messages: [],
};

export const CHAT_NAMES = {
  messages: 'messages',
};
