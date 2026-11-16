import { forwardRef, type ButtonHTMLAttributes } from "react";

/** Functional original example; merge styles with the host app's tokens. */
type Props = ButtonHTMLAttributes<HTMLButtonElement> & {
  busy?: boolean;
  variant?: "primary" | "secondary";
};

export const AccessibleActionButton = forwardRef<HTMLButtonElement, Props>(
  function AccessibleActionButton(
    { busy = false, variant = "primary", disabled, children, type = "button", ...rest },
    ref,
  ) {
    return (
      <button
        {...rest}
        ref={ref}
        type={type}
        disabled={disabled || busy}
        aria-busy={busy}
        data-variant={variant}
        className={`action-button ${rest.className ?? ""}`.trim()}
      >
        {busy && <span className="action-button__spinner" aria-hidden="true" />}
        <span>{children}</span>
      </button>
    );
  },
);
