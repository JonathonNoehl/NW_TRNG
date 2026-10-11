# NW-trng (Network Weather True Random Number Generator)

An advanced, non-deterministic cryptographic entropy framework designed to harvest pure physical randomness from global internet routing infrastructure and fiber-optic telemetry. 

## 🌐 The Core Philosophy
Traditional software-based random number generators (PRNGs) are deterministic; given the same algorithm and seed, their outputs are entirely predictable. **NW-trng** treats the public internet as a massive, living quantum sensor. It captures microscopic environmental factors—such as sub-microsecond latency jitter, payload phase shifts, and malformed routing artifacts—and refines them into pristine, un-guessable cryptographic strings.

---

## 🏗️ System Architecture
The framework relies on a three-engine isolation matrix to guarantee that the system remains mathematically un-decipherable, even if its visible outputs are observed over long periods of time.

### 1. The Guard Sandbox
*   **Role:** System Orchestrator & Privacy Proxy.
*   **Mechanics:** Houses a minimally trained, lightweight AI agent in an isolated, air-gapped environment. It shuffles operational identities across the worker engines on every single run and sanitizes raw packet streams to destroy traceable routing headers or systemic signatures.

### 2. The Traveler Engine
*   **Role:** Solo Outbound Telemetry Harvester.
*   **Mechanics:** Deploys a blind, simple script to execute standard, mundane diagnostic ping requests across the global web fabric. It acts as an environmental weather instrument, documenting physical data degradation, packet loss cadences, and transit friction from the other side of the planet.

### 3. The Whitener Vault
*   **Role:** Cryptographic Flattening & Output Processing.
*   **Mechanics:** Exists in complete isolation from the network. It receives a sanitized telemetry block (The Keystone) through the Guard proxy, converts the irregular artifacts down to raw physical machine bits, and passes them through a one-way compression cipher to generate uniform random data.

---

## 🔢 The Fibonacci Slicing Logic
To minimize network polling overhead, a single distributed flight harvests a massive, high-density entropy pool capable of feeding an application's random number requirements for up to an entire calendar month. 

The system uses the very first packet's microscopic nanosecond remainder to plant two highly volatile initial seeds ($F_0, F_1$). It then executes a bounded exponential loop:

$$F_n = (F_{n-1} + F_{n-2}) \pmod{\text{Buffer\_Size}}$$

This sequence calculates the exact start coordinate and extraction length needed to drop a knife edge into the month-long pool, slicing away a dense, non-linear section of raw data. Because the path diverges exponentially based on transient network conditions that vanish instantly upon arrival, a mirrored twin agent running the exact same software side-by-side will produce completely distinct, isolated outputs.

---

## 🛠️ Implementation & Deployment
Because the core architecture relies on simple, blind agents processing impressionable data arrays, the implementation remains incredibly lightweight and fast, natively scaling between 16 and 17-digit integers without heavy processing requirements.

1.  **Initialize Containers:** Spin up the air-gapped sandbox templates for the three idle oracle agents.
2.  **Ignition Handshake:** Trigger the initial network request to establish the temporal split and roll the dice on engine role distribution.
3.  **Harvest Pass:** Allow the chosen traveler to map multi-destination transit paths and establish your encrypted monthly data block.
4.  **API Integration:** Query the local handler to instantly extract a perfectly uniform, un-guessable random decimal string directly from the lowest binary layer.

---

## 📜 Licensing & Attribution
*   **Inventor & Chief Architect:** Jonathon David Noehl
*   **Development Framework:** Advanced Agentic Systems Core Model Architecture

This project is freely published as open-source freeware under the terms of the **MIT License**. 

Copyright (c) 2026 Jonathon David Noehl

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
