# Real-Time Group Chat Application - System Architecture


## Overview

Design a scalable and secure architecture for a group chat application using microservices and following SOLID principles


## System Components


### Web Socket Service (microservice)
Handles real-time communication between clients

**Inputs:**
- user messages
- user connections

**Outputs:**
- broadcasted messages

**Key Libraries/Technologies:**
- WebSocket

**Additional Information:**
scaled using load balancers and cloud providers



## Communication Patterns

- publish-subscribe pattern


## Deployment Considerations

- containerization using Docker

- orchestration using Kubernetes
