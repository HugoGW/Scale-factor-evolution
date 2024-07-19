# Scale-factor-evolution

$\textbf{I - Friedmann's equations}$

In this paper, I won't do the derivation from the Einstein field equations $R_{\mu \nu} - \frac{1}{2} R g_{\mu \nu} + \Lambda g_{\mu \nu} = \frac{8 \pi G}{c^4} T_{\mu \nu}$ to the Friedmann's equations :

$$(1) ~~~~~~~~ \frac{\dot{a}^2}{a^2} = \frac{8 \pi G}{3} \rho - \frac{k}{a^2} + \frac{\Lambda}{3}$$
$$(2) ~~~~~~~~ \frac{\ddot{a}}{a} = - \frac{4 \pi G}{3} (\rho + 3P) + \frac{\Lambda}{3}$$

but we also can specify the law of continuity : $\dot{\rho} = -3 \frac{\dot{a}}{a}(\rho + P) ~~~~~~ (3)$
So from these equations, we're going to compute the numerical solution from a differential equation we're going to derivate.

We also can consider others parameters such as the Hubble constant : $H_0 = H(0) = \frac{\dot{a}(0)}{a(0)}$,
the deceleration parameter $q_0 = q(0) = \big( \frac{\ddot{a}a}{\dot{a}^2} \big)_0$
and the critical density $\rho_c(0) = \rho_{c,0} = \frac{3 H_0^2}{8 \pi G}$

$\textbf{II - Content components of the Universe}$

For a Universe mainly constitutes of a certain content, the evolution of the scale factor will be given by their state equations.

- for the matter : $\rho_M(t) \propto a(t)^{-3}$
- for the radiation : $\rho_R(t) \propto a(t)^{-4}$
- for the dark energy : $\rho_{\Lambda}(t) \propto e^{\sqrt{{\Lambda}{3}t}}$

  
